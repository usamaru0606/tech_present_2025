import type { newUserInfo } from "~/model/userinfo";
import { AddUserServise } from "~/services/addUser";

export const useAddUser = () => {
  const Execute = async (newUserInfo: any) => {
    const userInfo: newUserInfo = {
      firstName: newUserInfo.firstName,
      lastName: newUserInfo.lastName,
      gender: newUserInfo.gender,
      age: newUserInfo.age,
      birthday: newUserInfo.birthday,
      mailAddress: newUserInfo.mailAddress,
      password: newUserInfo.password,
    };

    return AddUserServise(userInfo);
  };

  return {
    Execute,
  };
};
