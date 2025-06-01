export const LoginViewModel = () => {
  const router = useRouter();
  const userStore = useUserStore();
  const loginInfo = reactive({
    mailaddress: "",
    password: "",
  });

  onMounted(async () => {
  const savedMailaddress = localStorage.getItem('saved_mailAddress');
  const savedPassword = localStorage.getItem('saved_password');
  
  if (savedMailaddress && savedPassword) {
    loginInfo.mailaddress = savedMailaddress
    loginInfo.password = savedPassword
    try {
      const user = await useLogin().Execute(loginInfo);
      userStore.setUser(user);
      error.value = "";

      if (user && autoLogin.value) { SaveLoginInfo(); }

      await router.push("/");
    } catch {
      error.value = "自動ログインに失敗しました";
    }
  }
});

  const error = ref("");
  const autoLogin = ref(false)

  const Login = async () => {
    try {
      const user = await useLogin().Execute(loginInfo);
      userStore.setUser(user);
      error.value = "";

      if (user && autoLogin.value) { SaveLoginInfo(); }

      await router.push("/");
    } catch {
      error.value = "メールアドレスまたはパスワードが間違っています";
    }
  };

  const GoRegisterPage = async () => {
    await router.push("/register");
  };

  const SaveLoginInfo = () => {
    localStorage.setItem('saved_mailAddress', loginInfo.mailaddress);
    localStorage.setItem('saved_password', loginInfo.password);
  };

  return {
    loginInfo,
    error,
    autoLogin,
    Login,
    GoRegisterPage,
  };
};
