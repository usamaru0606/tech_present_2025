import type { LoginForm } from "~/model/loginform";

export const LoginViewModel = () => {
  const router = useRouter();

  const loginForm = reactive<LoginForm>({
    email: "",
    password: "",
  });
  const error = ref("");

  const Validate = (): boolean => {
    if (loginForm.email === "test" && loginForm.password === "test") {
      error.value = ""
      return true
    }
    error.value = "メールアドレスまたはパスワードが間違っています";
    return false
  }

  const Login = async () => {
    if (!Validate()) {
      return
    }
    await router.push("/");
  };

  const GoRegisterPage = async () => {
    await router.push("/register");
  };

  return {
    loginForm,
    error,
    Login,
    GoRegisterPage,
  };
};
