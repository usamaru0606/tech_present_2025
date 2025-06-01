// stores/user.ts
import type { UserInfo } from '~/model/userinfo';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null as UserInfo | null,
  }),
  getters: {
    isLoggedIn: (state) => !!state.user,
  },
  actions: {
    setUser(userInfo: UserInfo) {
      this.user = userInfo;
    },
    clearUser() {
      this.user = null;
    },
  },
});