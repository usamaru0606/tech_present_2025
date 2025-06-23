import { useRouter } from "vue-router";

export const RegisterViewModel = () => {
  const router = useRouter();
  const today = new Date();

  const genderItems = ["男性", "女性", "その他"];
  const step = ref(0);
  const error = ref("");
  const passwordConfirm = ref("");
  const expandedIndex = ref<number | null>(null);

  const birthdayItems = reactive({
    year: today.getFullYear(),
    month: today.getMonth() + 1,
    day: today.getDate(),
  });

  const goalDateInput = reactive({
    year: today.getFullYear(),
    month: today.getMonth() + 1,
    day: today.getDate(),
  });

  const problemOptions = [
    "",
    "体重を減らしたい",
    "筋肉をつけたい",
    "健康を維持したい",
    "生活習慣を改善したい",
    "その他",
  ];

  const userInfo = reactive({
    firstName: "",
    lastName: "",
    gender: "",
    age: 0,
    birthday: today,
    mailAddress: "",
    password: "",
    height: 100,
    weight: 40,
    startDate: today.toLocaleDateString("ja-JP", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }) as string | null,
    selectedProblem: "" as string | null,
    goalWeight: 0 as number | null,
    goaldate: "" as string | null,
  });

  const UpdateBirthday = () => {
    const { year, month, day } = birthdayItems;

    if (!year || !month || !day) {
      userInfo.age = 0;
      return;
    }

    const date = new Date(year, month - 1, day);
    userInfo.birthday = date;
    userInfo.age = CalculateAge(date);
  };

  const CalculateAge = (birthday: Date): number => {
    const current = new Date();
    let age = current.getFullYear() - birthday.getFullYear();

    const isBeforeBirthday =
      current.getMonth() < birthday.getMonth() ||
      (current.getMonth() === birthday.getMonth() &&
        current.getDate() < birthday.getDate());

    if (isBeforeBirthday) age--;

    return age;
  };

  const ValidateBasicInfo = (): boolean => {
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

  const ValidateGoalSetting = (): boolean => {
    if (expandedIndex.value != null) {
      if (
        !userInfo.selectedProblem ||
        !userInfo.goalWeight ||
        !goalDateInput.year ||
        !goalDateInput.month ||
        !goalDateInput.day
      ) {
        error.value = "すべての項目を入力してください";
        return false;
      }
    }
    error.value = "";
    return true;
  };

  const Validate = (): boolean => {
    if (step.value === 1) {
      return ValidateGoalSetting();
    }
    return ValidateBasicInfo();
  };

  const SetGoalItems = () => {
    if (expandedIndex.value == null) {
      userInfo.startDate = null;
      userInfo.selectedProblem = null;
      userInfo.goalWeight = null;
      userInfo.goaldate = null;
    } else {
      const { year, month, day } = goalDateInput;
      userInfo.goaldate = new Date(year, month - 1, day).toLocaleDateString(
        "ja-JP",
        {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
        }
      );
    }
  };

  const NextStep = () => {
    if (!Validate()) return;
    step.value++;
  };

  const RegisterUserInfo = async () => {
    if (!Validate()) return;
    SetGoalItems();

    try {
      const res = await useAddUser().Execute(userInfo);
      if (!res) {
        error.value = "登録に失敗しました";
        return;
      }
      await router.push("/login");
    } catch (e) {
      error.value = "登録に失敗しました";
    }
  };

  return {
    step,
    error,
    passwordConfirm,
    expandedIndex,
    birthdayItems,
    goaldate: goalDateInput,
    genderItems,
    problemOptions,
    userInfo,
    UpdateBirthday,
    RegisterUserInfo,
    NextStep,
  };
};
