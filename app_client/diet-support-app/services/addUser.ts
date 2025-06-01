import type { newUserInfo } from "~/model/userinfo";

export const AddUserServise = async (newUserInfo: newUserInfo) => {
  const res = await useFetch("http://127.0.0.1:8000/user/add", {
    method: "POST",
    body: {
      firstName: newUserInfo.firstName,
      lastName: newUserInfo.lastName,
      gender: newUserInfo.gender,
      age: newUserInfo.age,
      birthday: newUserInfo.birthday,
      mailAddress: newUserInfo.mailAddress,
      password: newUserInfo.password,
    },
  });

  if (res.error.value) throw new Error(res.error.value.message);

  return;
};
