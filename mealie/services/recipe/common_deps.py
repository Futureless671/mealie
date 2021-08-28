from typing import Any

from fastapi import BackgroundTasks, Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from mealie.db.db_setup import generate_session
from mealie.core.dependencies import get_current_user, is_logged_in


class CommonDeps(BaseModel):
    session: Session
    background_tasks: BackgroundTasks
    user: Any

    class Config:
        arbitrary_types_allowed = True


def read_deps(
    background_tasks: BackgroundTasks,
    session: Session = Depends(generate_session),
    current_user=Depends(is_logged_in),
):
    return CommonDeps(
        session=session,
        background_tasks=background_tasks,
        user=current_user,
    )


def write_deps(
    background_tasks: BackgroundTasks,
    session: Session = Depends(generate_session),
    current_user=Depends(get_current_user),
):
    return CommonDeps(
        session=session,
        background_tasks=background_tasks,
        user=current_user,
    )
