# Rotas de autenticação vai ficar aqui

from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.usuarios import Usuario
from app.auth import hash_senha, verificar_senha, criar_token

# APIRouter agrupa as rotas dentro desse moduçp com o prefixo / auth
router = APIRouter(prefix = "/auth" , tags = ["Autenticação"])
templates = Jinja2Templates(directory = "app/templates")

#TELA DE CADASTRO
@router.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "/auth/cadastro.html",
        {"request": request}
    )

#TELA DE LOGIN
@router.get("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "/auth/login.html",
        {"request": request}    
    )

#ROTA PARA CRIAR O USUARIO
@router.post("/cadastro")
def fazer_cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    # TODA ROTA QUE FAZER PARA GUARDAR CADASTRO OU LOGIN SLA VOU PRECISAR DESSE db.
    db: Session = Depends(get_db)
):
    #VERIFICAR SE O EMAIL JA ESTÁ CADASTRADO
    usuario_existente = db.query(Usuario).filter_by(email = email).first()
    #MENSAGEM DE ERRO SE O EMAIL ESTIVER CADASTRADO
    if usuario_existente:
        return templates.TemplateResponse(
            request,
            "/auth/cadastro.html",
            {"request": request , "erro": "Este E-mail já está cadastrado"}
        )
    #CRIAR O USUARIO - CRIAR O OBJETO
    novo_usuario= Usuario(
        nome=nome,
        email=email,
        senha_hash=hash_senha(senha),
    )
    db.add(novo_usuario)
    db.commit()
    return RedirectResponse(url = "/auth/login" , status_code = 302)

# Fazer o login
@router.post("/login")
def fazer_login(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    # 1. Busca o usuário pelo email no db

    # 2. Verificar a senha com bcrypt

    # 3. Gera o token JWT

    # 4. Salvar o token em um cookie e redirecionar para página home

# 1. Busca o usuário pelo email no db
usuario = db.query(Usuario).filter_by(email=email).first()


# 2. Verificar a senha com bcrypt

# 3. Gera o token JWT

# 4. Salvar o token em um cookie e redirecionar para página home