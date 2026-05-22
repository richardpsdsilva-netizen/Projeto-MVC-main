# Instalar as bibliotecas 

no terminal:
```bash
pip install -r requirements.txt
```

# INICIALIZAR O ALEMBIC
NO TERMINAL:
```bash
python -m alembic init migration

```

# EDITAR O ARQUIVO ALEMBIC INIT - NA LINHA 89:
sqlalchemy.url = 

# NA VIDA REAL NAO SOBE O ENV PRO GIT HUB

# GERAR A MIGRATION
NO TERMINAL:
```bash
python -m alembic revision --autogenerate -m "criar a tabela usuarios"

```

# APLICAR A MIGRATION NO BANCO
```bash
python -m alembic upgrade head
```

# JWT


# RODAR O CODIGO 
```bash
python -m uvicorn app.main:app --reload
```