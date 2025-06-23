from sqlalchemy.orm import Session
from app.models.goal import GoalSetting
from app.schemas.goal import GoalSettingCreate, GoalSettingUpdate
from datetime import datetime

def create_goal_setting(db: Session, goal_setting: GoalSettingCreate) -> GoalSetting:
    """
    新しい目標設定をデータベースに作成する

    Args:
        db (Session): データベースセッション
        goal_setting (GoalSettingCreate): 作成する目標設定データ

    Returns:
        GoalSetting: 作成された目標設定オブジェクト
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
        return db_goal_setting
    except Exception as e:
        db.rollback()
        raise e

def update_goal_setting(db: Session, user_id: str, goal_setting_update: GoalSettingUpdate) -> GoalSetting:
    """
    既存の目標設定を更新する

    Args:
        db (Session): データベースセッション
        user_id (str): ユーザーID
        goal_setting_update (GoalSettingUpdate): 更新する目標設定データ

    Returns:
        GoalSetting: 更新された目標設定オブジェクト

    Raises:
        ValueError: 指定されたIDの目標設定が見つからない場合
    """
    db_goal_setting = db.query(GoalSetting).filter(GoalSetting.user_id == user_id).first()
    if not db_goal_setting:
        # 新規作成
        new_goal = GoalSetting(
            user_id=user_id,
            height=getattr(goal_setting_update, "height", 0) or 0,
            weight=getattr(goal_setting_update, "weight", 0) or 0,
            problem={"name": getattr(goal_setting_update, "problem", None)} if getattr(goal_setting_update, "problem", None) else {},
            deadline=datetime.strptime(getattr(goal_setting_update, "goalDate", None), "%Y/%m/%d").date() if getattr(goal_setting_update, "goalDate", None) else None,
            goal_weight=getattr(goal_setting_update, "goalWeight", 0) or 0,
        )
        db.add(new_goal)
        db.commit()
        db.refresh(new_goal)
        return new_goal

    update_data = goal_setting_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        # フロントエンドとバックエンドのキー名が異なる場合のマッピング
        if key == "goalDate":
            setattr(db_goal_setting, "deadline", datetime.strptime(value, "%Y/%m/%d").date() if value else None)
        elif key == "goalWeight":
            setattr(db_goal_setting, "goal_weight", value)
        elif key == "startDate":
            setattr(db_goal_setting, "start_date", datetime.strptime(value, "%Y/%m/%d").date() if value else None)
        else:
            setattr(db_goal_setting, key, value)
            
    db.commit()
    db.refresh(db_goal_setting)
    return db_goal_setting

def get_goal_setting_by_user_id(db: Session, user_id: str):
    """
    ユーザーIDから目標設定を取得する
    """
    return db.query(GoalSetting).filter(GoalSetting.id == user_id).first() 