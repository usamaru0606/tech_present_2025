import { useRouter } from "vue-router";

export const LoginViewModel = () => {
  const router = useRouter();
  const userIdStore = useUserIdStore();

  const loginInfo = reactive({
    mailaddress: "",
    password: "",
  });

  const error = ref("");
  const autoLogin = ref(false);

  const LOCAL_STORAGE_KEYS = {
    mail: "saved_mailAddress",
    pass: "saved_password",
  };

  const loadSavedCredentials = () => {
    const savedMail = localStorage.getItem(LOCAL_STORAGE_KEYS.mail);
    const savedPass = localStorage.getItem(LOCAL_STORAGE_KEYS.pass);

    if (savedMail && savedPass) {
      loginInfo.mailaddress = savedMail;
      loginInfo.password = savedPass;
      autoLogin.value = true; // UI に反映したい場合
      Login();
    }
  };

  const saveLoginInfo = () => {
    localStorage.setItem(LOCAL_STORAGE_KEYS.mail, loginInfo.mailaddress);
    localStorage.setItem(LOCAL_STORAGE_KEYS.pass, loginInfo.password);
  };

  const Login = async () => {
    try {
      // 仮ログイン（テスト用）
      if (loginInfo.mailaddress === "test" && loginInfo.password === "test") {
        userIdStore.setUserId("test");
        error.value = "";
        await router.push("/");
        return;
      }

      const userId = await useLogin().Execute(loginInfo);

      if (!userId) {
        error.value = "ログインに失敗しました";
        return;
      }

      userIdStore.setUserId(userId);
      error.value = "";

      if (autoLogin.value) {
        saveLoginInfo();
      }

      await router.push("/");
    } catch (e) {
      console.error("ログインエラー:", e);
      error.value = "ログインに失敗しました";
    }
  };

  const GoToRegisterPage = () => {
    router.push("/register");
  };

  onMounted(loadSavedCredentials);

  return {
    loginInfo,
    error,
    autoLogin,
    Login,
    GoToRegisterPage,
  };
};
