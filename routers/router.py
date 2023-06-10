from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from auth.auth_database import get_async_session
from tables.table_models import trade_post
from tables.music_trade_post_model import Music_post_trade

router = APIRouter(
    prefix='/select_type',
    tags=['Operation']

)


# routers are used to separate logic in your code, it is bad idea to use all routers in one 'main.py' file.
# for example, in a big project, you have to separate all stuff like this,
# cuz it is much easier to find things if needed


# in this case we are using ORM query

@router.post('/post_trade')
async def post_trade(new_post_trade: Music_post_trade, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(trade_post).values(**new_post_trade.dict())
        await session.execute(stmt)
        await session.commit()
        return {'status': 'your trade posted successfully'}
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'Error',
            'data': None,
            'details': None
        })


@router.get('/get_items')
async def get_items(
        item_type: str = None,
        item_price: int = None,
        min_price: int = None,
        max_price: int = None,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(trade_post)
        if item_type is not None:
            query = query.where(trade_post.c.type == item_type)
        if item_price is not None:
            query = query.where(trade_post.c.price == item_price)
        if min_price is not None:
            query = query.where(trade_post.c.price >= min_price)
        if max_price is not None:
            query = query.where(trade_post.c.price <= max_price)

        result = await session.execute(query)
        items = [dict(row._asdict()) for row in result]
        return items
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'Error',
            'data': None,
            'details': None
        })

