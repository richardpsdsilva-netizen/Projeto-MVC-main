import os
from pathlib import Path
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.auth import get_usuario_opicional
# 1. Importe o router do seu controller
from app.controllers.auth_controller import router as auth_router

# 2. Inicialize o app apenas UMA vez
app = FastAPI(title="Sistema de Ponto de Venda")

# 3. Descobre o caminho absoluto para a pasta onde este main.py está
BASE_DIR = Path(__file__).resolve().parent

# Configura os caminhos absolutos para static e templates
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# (Opcional) Garante que as pastas existam para não dar erro caso esqueça de criá-las
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

# 4. CONFIGURAR A PASTA PARA SERVIR OS ARQUIVOS ESTÁTICOS
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# 5. CONFIGURAR O JINJA2 PARA RENDERIZAR OS HTML
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# 6. Registre o roteador na instância principal do app
app.include_router(auth_router)

@app.get("/")
def raiz():
    return {"message": "API Online"}

#Toda tela Get
@app.get("/")
def tela_inicial(
    request: Request,
    usuario = Depends(get_usuario_opicional)
):
     #tela nao logado
    if usuario is None:
        #tela nao logado
        return templates.TemplateResponse(
            request,
            "index.html",
            {"request": request}
        )
    #Logado - exibir a tela de funcionario
    return templates.TemplateResponse(
        request,
        "home.html",
        {"request": request"usuario": usuario}
    )