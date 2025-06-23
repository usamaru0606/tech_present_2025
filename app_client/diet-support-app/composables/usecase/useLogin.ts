import type { LoginForm } from "~/model/loginform";
import { LoginService } from "~/services/login";

export const useLogin = () => {
  const Execute = async (loginInfo: LoginForm) => {
    return LoginService(loginInfo);
  };

  return {
    Execute,
  };
};
