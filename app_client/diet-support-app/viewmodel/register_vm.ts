import { useRouter } from "vue-router";

export const RegisterViewModel = () => {
  const router = useRouter();
  const today = new Date();

  const genderItems = ["男性", "女性", "その他"];
  const step = ref(1);
  const error = ref("");
  const passwordConfirm = ref("");

  const birthdayItems = reactive({
    year: today.getFullYear(),
    month: today.getMonth() + 1,
    day: today.getDate(),
  });

  const userInfo = reactive({
    firstName: "",
    lastName: "",
    gender: "",
    age: 0,
    birthday: today,
    mailAddress: "",
    password: "",
  });

  const UpdateBirthday = () => {
    const { year, month, day } = birthdayItems;

    // 有効な日付かチェック
    if (!year || !month || !day) {
      userInfo.age = 0;
      return;
    }

    const date = new Date(year, month - 1, day);
    userInfo.birthday = date;
    userInfo.age = CalculateAge(date);
  };

  const CalculateAge = (birthday: Date): number => {
    let age = today.getFullYear() - birthday.getFullYear();
    const isBeforeBirthday =
      today.getMonth() < birthday.getMonth() ||
      (today.getMonth() === birthday.getMonth() &&
        today.getDate() < birthday.getDate());
    if (isBeforeBirthday) age--;
    return age;
  };

  const Validate = (): boolean => {
    const { firstName, lastName, gender, birthday, mailAddress, password } =
      userInfo;

    if (
      !firstName ||
      !lastName ||
      !gender ||
      !birthday ||
      !mailAddress ||
      !password ||
      !passwordConfirm.value
    ) {
      error.value = "すべての項目を入力してください";
      return false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(mailAddress)) {
      error.value = "メールアドレスの形式が正しくありません";
      return false;
    }

    if (password !== passwordConfirm.value) {
      error.value = "パスワードと確認用パスワードが一致しません";
      return false;
    }

    if (userInfo.age <= 0) {
      error.value = "生年月日を正しく入力してください";
      return false;
    }

    error.value = "";
    return true;
  };

  const RegisterUser = async (onSuccess: () => void) => {
    if (!Validate()) return;

    try {
      const result = await useAddUser().Execute(userInfo);
      if (!result) {
        error.value = "登録に失敗しました";
        return;
      }
      onSuccess();
    } catch (e) {
      console.error("登録エラー:", e);
      error.value = "登録に失敗しました";
    }
  };

  const RegisterGoal = () => {
    RegisterUser(() => router.push("/registersub"));
  };

  const RegisterUserInfo = () => {
    RegisterUser(() => step.value++);
  };

  return {
    passwordConfirm,
    birthdayItems,
    genderItems,
    userInfo,
    error,
    step,
    RegisterGoal,
    RegisterUserInfo,
    UpdateBirthday,
  };
};
