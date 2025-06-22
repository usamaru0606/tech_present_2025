import type { GoalSettingItems } from "~/model/goalsettingitem";
import type { UserInfo } from "~/model/userinfo";

export const AddUserService = async (
  newUserInfo: UserInfo & GoalSettingItems
) => {
  try {
    const res = await $fetch("http://127.0.0.1:8000/user/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        firstName: newUserInfo.firstName,
        lastName: newUserInfo.lastName,
        gender: newUserInfo.gender,
        age: newUserInfo.age,
        birthday: newUserInfo.birthday,
        mailAddress: newUserInfo.mailAddress,
        password: newUserInfo.password,
        height: newUserInfo.height,
        weight: newUserInfo.weight,
        startDate: newUserInfo.startDate,
        problem: newUserInfo.problem,
        goalWeight: newUserInfo.goalWeight,
        goalDate: newUserInfo.goalDate,
      }),
    });

    return res;
  } catch {
    return false;
  }
};
