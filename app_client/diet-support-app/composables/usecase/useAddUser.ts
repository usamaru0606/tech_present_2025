import type { GoalSettingItems } from "~/model/goalsettingitem";
import type { UserInfo } from "~/model/userinfo";
import { AddUserService } from "~/services/addUser";
import { CreateGoalSettingService } from "~/services/goalsetting";
import { DeleteUserService } from "~/services/deleteUser";

export const useAddUser = () => {
  const Execute = async (newUserInfo: any) => {
    const userInfo: UserInfo & GoalSettingItems = {
      userId: newUserInfo.userId,
      firstName: newUserInfo.firstName,
      lastName: newUserInfo.lastName,
      gender: newUserInfo.gender,
      age: newUserInfo.age,
      birthday: newUserInfo.birthday.toLocaleDateString("ja-JP", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }),
      mailAddress: newUserInfo.mailAddress,
      password: newUserInfo.password,
       height: newUserInfo.height,
      weight: newUserInfo.weight,
      startDate: newUserInfo.startDate,
      problem: newUserInfo.selectedProblem,
      goalWeight: newUserInfo.goalWeight,
      goalDate: newUserInfo.goalDate,
    };

    // 1. ユーザー登録
    const userRes = await AddUserService(userInfo);
    if (!userRes || !userRes.guid) return false;

    // 2. 目標設定登録
    const goalSettingRes = await CreateGoalSettingService({
      userId: userRes.guid,
      height: userInfo.height,
      weight: userInfo.weight,
      problem: userInfo.problem,
      startDate: userInfo.startDate,
      goalDate: userInfo.goalDate,
      goalWeight: userInfo.goalWeight,
    });
    if (!goalSettingRes) {
      // 目標設定登録失敗時はユーザー登録をロールバック
      await DeleteUserService(userRes.guid);
      return false;
    }

    return userRes;
  };

  return {
    Execute,
  };
};
