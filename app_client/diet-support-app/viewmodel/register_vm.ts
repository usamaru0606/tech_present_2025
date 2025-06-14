export const RegisterViewModel = () => {
  const router = useRouter();
  const passwordConfirm = ref("");
  const genderItems = ["男性", "女性", "その他"];
  const today = new Date();
  const birthdayItems = reactive({
    year: new Date().getFullYear(),
    month: new Date().getMonth() + 1,
    day: new Date().getDate(),
  });
  const userInfo = reactive({
    firstName: "",
    lastName: "",
    gender: "",
    age: 0,
    birthday: today,
    mailAddress: "",
    password: "",
    signinDate: today.toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }),
    height: 100,
    weight: 40,
  });
  const error = ref("");
  const step = ref(1);

  const Register = async () => {
    if (!Validate()) return;

    try {
      const res = await useAddUser().Execute(userInfo);
      if (!res) return (error.value = "登録に失敗しました");
      await router.push("/login");
    } catch (e) {
      error.value = "登録に失敗しました";
    }
  };

  const NextStep = async () => {
    if (!Validate()) return;
    step.value++;
  };

  const Validate = (): boolean => {
    if (
      !userInfo.firstName ||
      !userInfo.lastName ||
      !userInfo.gender ||
      !userInfo.birthday ||
      !userInfo.mailAddress ||
      !userInfo.password ||
      !passwordConfirm
    ) {
      error.value = "すべての項目を入力してください";
      return false;
    }

    if (
      !userInfo.mailAddress.includes("@") ||
      !userInfo.mailAddress.includes(".")
    ) {
      error.value = "メールアドレスの形式が正しくありません";
      return false;
    }

    if (userInfo.password !== passwordConfirm.value) {
      error.value = "パスワードと確認用パスワードが一致しません";
      return false;
    }

    if (userInfo.age < 0) {
      error.value = "生年月日を正しく入力してください";
      return false;
    }

    error.value = "";
    return true;
  };

  const UpdateBirthday = async () => {
    const year = Number(birthdayItems.year);
    const month = Number(birthdayItems.month);
    const day = Number(birthdayItems.day);

    // 入力がすべて有効な数字か確認
    if (!year || !month || !day) {
      userInfo.age = 0;
      return;
    }

    userInfo.birthday = new Date(year, month - 1, day);
    userInfo.age = await CalculateAge();
  };

  async function CalculateAge(): Promise<number> {
    if (!birthdayItems.year || !birthdayItems.month || !birthdayItems.day) {
      return 0;
    }

    let age = today.getFullYear() - userInfo.birthday.getFullYear();
    const isNotYetBirthday =
      today.getMonth() < userInfo.birthday.getMonth() ||
      (today.getMonth() === userInfo.birthday.getMonth() &&
        today.getDate() < userInfo.birthday.getDate());
    if (isNotYetBirthday) age--;

    return age;
  }

  return {
    passwordConfirm,
    birthdayItems,
    genderItems,
    userInfo,
    error,
    step,
    NextStep,
    Register,
    UpdateBirthday,
  };
};
