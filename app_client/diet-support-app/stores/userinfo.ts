import type { UserInfo } from "~/model/userinfo"

// stores/userInfo.ts
export const useUserInfoStore = defineStore('userInfo', {
  state: (): { userInfo: UserInfo } => ({
    userInfo: {
      firstName: '',
      lastName: '',
      gender: '',
      age: 0,
      birthday: '',
      mailAddress: '',
      password: '',
    },
  }),
  actions: {
    setUserInfo(info: Partial<UserInfo>) {
      this.userInfo = { ...this.userInfo, ...info }
    },
    clearUserInfo() {
      this.userInfo = {
        firstName: '',
        lastName: '',
        gender: '',
        age: 0,
        birthday: '',
        mailAddress: '',
        password: '',
      }
    },
  },
})
