from fastapi import APIRouter

from app.services import handover as svc

router = APIRouter(prefix="/reconcile", tags=["交班对账"])


@router.get("")
def get_reports():
    return svc.list_reconcile()


@router.get("/{plan_id}")
def get_plan_proof(plan_id: int):
    """按计划 id 查询并集证明（只读）：物化报告链 + 同源实时校验。"""
    return svc.get_plan_proof(plan_id)
