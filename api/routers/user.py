from fastapi import APIRouter
from typing import List
from crawlers.extratoclube import ExtratoClube

router = APIRouter()

@router.get("/benefits/{cpf}")
async def get_benefits(cpf: str) -> List[str]:
    extrato_clube = ExtratoClube(cpf, "testekonsi", "testekonsi")
    extrato_clube.login()
    extrato_clube.close_modal()
    extrato_clube.access_reports()
    extrato_clube.search_benefits_by_cpf()
    return extrato_clube.access_benefits_by_cpf()