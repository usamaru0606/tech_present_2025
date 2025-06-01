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
    birthday: '',
    mailAddress: '',
    password: '',
  })
  const error = ref('')

  const Register = async () => {
    if (!Validate()) return

    try {
      await useAddUser().Execute(userInfo);
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
    userInfo.age = await CalculateAge();
    userInfo.birthday = `${birthdayItems.year}-${String(birthdayItems.month).padStart(2, '0')}-${String(birthdayItems.day).padStart(2, '0')}`;
  };

  async function CalculateAge():Promise<number>{
    if(!birthdayItems.year || !birthdayItems.month || !birthdayItems.day){
      return 0;
    }
    const birthday = new Date(Number(birthdayItems.year),Number(birthdayItems.month) - 1, Number(birthdayItems.day));
    const today = new Date();

    let age = today.getFullYear() - birthday.getFullYear();
    const isNotYetBirthday = today.getMonth() < birthday.getMonth() ||  (today.getMonth() === birthday.getMonth() && today.getDate() < birthday.getDate());
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