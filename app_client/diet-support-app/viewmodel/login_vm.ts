import type { LoginForm } from "~/model/loginform";

export const LoginViewModel = () => {
  const loginForm = ref<LoginForm>({
    email: "",
    password: "",
  });

  const error = ref("");
  const router = useRouter();

  const Login = async () => {
    // 仮実装
    if (
      loginForm.value.email === "test" &&
      loginForm.value.password === "test"
    ) {
      await router.push("/");
    } else {
      error.value = "メールアドレスまたはパスワードが間違っています";
    }
  };

  const GoRegisterPage = async() => {
  await router.push("/register");
}

  return {
    loginForm,
    error,
    Login,
    GoRegisterPage
  };
};
