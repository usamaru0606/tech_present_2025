import type { LoginForm } from "~/model/loginform";

export const LoginService = async (loginForm: LoginForm):Promise<string|null> => {
  try {
    const res = await $fetch<{ guid: string }>("http://127.0.0.1:8000/api/user/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        mailAddress: loginForm.mailAddress,
        password: loginForm.password,
      }),
    });
    return res.guid;
  } catch (e) {
    console.log(e);
    return null;
  }
};
