import type { LoginForm } from "~/model/loginform";
import { LoginService } from "~/services/login";

export const useLogin = () => {
  const Execute = async (loginInfo: any) => {
    const loginform: LoginForm = {
      mailAddress: loginInfo.mailAddress,
      password: loginInfo.password,
    };

    return LoginService(loginform);
  };

  return {
    Execute,
  };
};
