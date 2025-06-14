from sqlalchemy.orm import Session
from app.models.goal import GoalSetting
from app.schemas.goal import GoalSettingCreate, GoalSettingUpdate

def create_goal_setting(db: Session, goal_setting: GoalSettingCreate) -> bool:
    """
    新しい目標設定をデータベースに作成する

    Args:
        db (Session): データベースセッション
        goal_setting (GoalSettingCreate): 作成する目標設定データ

    Returns:
        bool: 作成が成功したかどうか
    """
    db_goal_setting = GoalSetting(
        id=goal_setting.id,
        height=goal_setting.height,
        weight=goal_setting.weight,
        problem=goal_setting.problem,
        deadline=goal_setting.deadline,
        goal_weight=goal_setting.goal_weight
    )
    
    try:
        db.add(db_goal_setting)
        db.commit()
        db.refresh(db_goal_setting)
        return True
    except Exception as e:
        db.rollback()
        raise e

def update_goal_setting(db: Session, goal_setting: GoalSettingUpdate) -> bool:
    """
    既存の目標設定を更新する

    Args:
        db (Session): データベースセッション
        goal_setting (GoalSettingUpdate): 更新する目標設定データ

    Returns:
        bool: 更新が成功したかどうか

    Raises:
        HTTPException: 指定されたIDの目標設定が見つからない場合
    """
    try:
        db_goal_setting = db.query(GoalSetting).filter(GoalSetting.id == goal_setting.id).first()
        if not db_goal_setting:
            raise ValueError(f"Goal setting with id {goal_setting.id} not found")

        # 更新対象のフィールドを設定
        db_goal_setting.problem = goal_setting.problem
        db_goal_setting.deadline = goal_setting.deadline
        db_goal_setting.goal_weight = goal_setting.goal_weight

        db.commit()
        db.refresh(db_goal_setting)
        return True
    except Exception as e:
        db.rollback()
        raise e 