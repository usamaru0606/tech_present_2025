import type { newUserInfo } from "~/model/newuserinfo";
import { AddUserServise } from "~/services/addUser";

export const useAddUser = () => {
  const Execute = async (newUserInfo: any) => {
    const userInfo: newUserInfo = {
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
    };

    return AddUserServise(userInfo);
  };

  return {
    Execute,
  };
};
