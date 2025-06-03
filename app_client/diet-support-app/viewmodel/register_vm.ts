export const RegisterViewModel = () => {
  const router = useRouter();
  const passwordConfirm = ref('');
  const genderItems = ['男性', '女性', 'その他'];
  const birthdayItems = reactive({
    year:'',
    month:'',
    day:'',
  })
  const userInfo = reactive({
    firstName: '',
    lastName: '',
    gender: '',
    age: 0,
    birthday: new Date(),
    mailAddress: '',
    password: '',
  })
  const error = ref('')

  const Register = async () => {
    if (!Validate()) return;

    try {
      const res = await useAddUser().Execute(userInfo);
      if(!res) return error.value = '登録に失敗しました';
      await router.push('/login')
    } catch (e) {
      error.value = '登録に失敗しました'
    }
  }

  const Validate = (): boolean => {
    if (!userInfo.firstName || !userInfo.lastName || !userInfo.gender || !userInfo.birthday || !userInfo.mailAddress || !userInfo.password || !passwordConfirm) {
      error.value = 'すべての項目を入力してください'
      return false
    }

    if (userInfo.password !== passwordConfirm.value) {
      error.value = 'パスワードと確認用パスワードが一致しません'
      return false
    }

    error.value = ''
    return true
  }

  const UpdateBirthday = async () => {
    userInfo.birthday = new Date(Number(birthdayItems.year),Number(birthdayItems.month) - 1, Number(birthdayItems.day));
    userInfo.age = await CalculateAge();
  };

  async function CalculateAge():Promise<number>{
    if(!birthdayItems.year || !birthdayItems.month || !birthdayItems.day){
      return 0;
    }
    const today = new Date();

    let age = today.getFullYear() - userInfo.birthday.getFullYear();
    const isNotYetBirthday = today.getMonth() < userInfo.birthday.getMonth() ||  (today.getMonth() === userInfo.birthday.getMonth() && today.getDate() < userInfo.birthday.getDate());
    if(isNotYetBirthday) age--;

    return age
  }

  return {
    passwordConfirm,
    birthdayItems,
    genderItems,
    userInfo,
    error,
    Register,
    UpdateBirthday,
  }
}