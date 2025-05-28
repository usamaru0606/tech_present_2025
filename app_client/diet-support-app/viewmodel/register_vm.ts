import type { UserInfo } from '~/model/userinfo'
import{v4 as uuidv4} from 'uuid'

export const RegisterViewModel = () => {
  const form = ref<UserInfo>({
  guid: uuidv4(),
  name: '',
  gender:'',
  age:0,
  birthday:'',
  email: '',
  password: '',
  passwordConfirm: '',
  })

  const error = ref('')
  const router = useRouter()

  const validate = (): boolean => {
    if (
      !form.value.name ||
      !form.value.email ||
      !form.value.password ||
      !form.value.passwordConfirm
    ) {
      error.value = 'すべての項目を入力してください'
      return false
    }

    if (form.value.password !== form.value.passwordConfirm) {
      error.value = 'パスワードと確認用パスワードが一致しません'
      return false
    }

    error.value = ''
    return true
  }

  const Register = async () => {
    if (!validate()) return

    try {
      await router.push('/login')
    } catch (e) {
      error.value = '登録に失敗しました'
    }
  }

  return {
    form,
    error,
    Register,
  }
}
