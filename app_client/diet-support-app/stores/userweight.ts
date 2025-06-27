// stores/userweight.ts

export const useUserWeightStore = defineStore('userweight', {
  state: () => ({
    userWeight: null as number | null,
  }),
  actions: {
    setUserWeight(userWeight:number) {
      this.userWeight = userWeight;
    },
    clearUserWeight() {
      this.userWeight = null;
    },
    getUserWeight(): number | null{
      return this.userWeight;
    }
  },
});

export const useUserInitWeightStore = defineStore('userinitweight', {
  state: () => ({
    userWeight: null as number | null,
  }),
  actions: {
    setUserInitWeight(userWeight:number) {
      this.userWeight = userWeight;
    },
    clearUserInitWeight() {
      this.userWeight = null;
    },
    getUserInitWeight(): number | null{
      return this.userWeight;
    }
  },
});