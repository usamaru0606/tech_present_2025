import type { UserInfo } from '~/model/userinfo'
import{v4 as uuidv4} from 'uuid'

export const RegisterViewModel = () => {
  const router = useRouter()

  const userInfo = reactive<UserInfo>({
    guid: uuidv4(),
    name: '',
    gender: '',
    age: 0,
    birthday: '',
    email: '',
    password: '',
    passwordConfirm: '',
  })
  const error = ref('')
  
  const Validate = (): boolean => {
    if (!userInfo.name || !userInfo.email || !userInfo.password || !userInfo.passwordConfirm) {
      error.value = 'すべての項目を入力してください'
      return false
    }

    if (userInfo.password !== userInfo.passwordConfirm) {
      error.value = 'パスワードと確認用パスワードが一致しません'
      return false
    }

    error.value = ''
    return true
  }

  const Register = async () => {
    if (!Validate()) return

    try {
      // API 呼び出しなどの処理をここに追加
      await router.push('/login')
    } catch (e) {
      error.value = '登録に失敗しました'
    }
  }

  return {
    userInfo,
    error,
    Register,
  }
}