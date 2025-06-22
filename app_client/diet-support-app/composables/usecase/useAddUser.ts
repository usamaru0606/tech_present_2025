import type { GoalSettingItems } from "~/model/goalsettingitem";
import type { UserInfo } from "~/model/userinfo";
import { AddUserService } from "~/services/addUser";

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

    return AddUserService(userInfo);
  };

  return {
    Execute,
  };
};
