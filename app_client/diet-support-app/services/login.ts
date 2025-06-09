import type { LoginForm } from "~/model/loginform";

export const LoginServise = async (loginform: LoginForm) => {
  try {
    const res = await $fetch<string>("http://127.0.0.1:8000/user/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: loginform.mailAddress,
        password: loginform.password,
      }),
    });

    return res
  } catch {
    return null;
  }
};
