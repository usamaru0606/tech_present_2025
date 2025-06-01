import type { LoginForm } from "~/model/loginform";
import type { UserInfo } from "~/model/userinfo";

export const LoginServise = async (loginform: LoginForm) => {
  const res = await useFetch<UserInfo>("http://127.0.0.1:8000/users/", {
    method: "POST",
    body: {
      mailAddress: loginform.mailAddress,
      password: loginform.password,
    },
  });

  if (res.error.value) throw new Error(res.error.value.message);
  if (!res.data.value) throw new Error("ユーザー情報が取得できません");

  return res.data.value;
};
