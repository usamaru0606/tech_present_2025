export const LoginViewModel = () => {
  const router = useRouter();
  const userIdStore = useUserIdStore();
  const loginInfo = reactive({
    mailaddress: "",
    password: "",
  });
  const error = ref("");
  const autoLogin = ref(false);

  onMounted(async () => {
    const savedMailaddress = localStorage.getItem("saved_mailAddress");
    const savedPassword = localStorage.getItem("saved_password");

    if (savedMailaddress && savedPassword) {
      loginInfo.mailaddress = savedMailaddress;
      loginInfo.password = savedPassword;
      Login();
    }
  });

  const Login = async () => {
    try {
      const userId = await useLogin().Execute(loginInfo);
      if(!userId) return  error.value = "ログインに失敗しました";
      userIdStore.setUserId(userId);
      error.value = "";

      if (userId && autoLogin.value) {
        SaveLoginInfo();
      }

      await router.push("/");
    } catch {
      error.value =  "ログインに失敗しました";
    }
  };

  const GoRegisterPage = async () => {
    await router.push("/register");
  };

  const SaveLoginInfo = () => {
    localStorage.setItem("saved_mailAddress", loginInfo.mailaddress);
    localStorage.setItem("saved_password", loginInfo.password);
  };

  return {
    loginInfo,
    error,
    autoLogin,
    Login,
    GoRegisterPage,
  };
};
