from uuid import uuid4

from fastapi import APIRouter, Body, status

from atleta.models import AtletaModel
from categorias.models import CategoriaModel
from categorias.schemas import CategoriaIn, CategoriaOut
from contrib.dependencies import DatabaseDependency

router = APIRouter()


@router.post(
    "/",
    summary="Cria uma Categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def create_category(
    db_session: DatabaseDependency, categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out
