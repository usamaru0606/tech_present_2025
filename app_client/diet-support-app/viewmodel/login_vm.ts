export const LoginViewModel = () => {
  const router = useRouter();
  const userStore = useUserStore();
  const loginInfo = reactive({
    mailaddress: "",
    password: "",
  });

  const error = ref("");

  const Login = async () => {
    try {
      const user = await useLogin().Execute(loginInfo);
      userStore.setUser(user);
      error.value = "";
      await router.push("/");
    } catch {
      error.value = "メールアドレスまたはパスワードが間違っています";
    }
  };

  const GoRegisterPage = async () => {
    await router.push("/register");
  };

  return {
    loginInfo,
    error,
    Login,
    GoRegisterPage,
  };
};
