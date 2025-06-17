import type { newUserInfo } from "~/model/newuserinfo";

export const AddUserServise = async (newUserInfo: newUserInfo) => {
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
      }),
    });

    return res;
  } catch {
    return false;
  }
};
