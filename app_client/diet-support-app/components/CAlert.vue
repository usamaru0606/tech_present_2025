<template>
  <v-alert
    :class="{ invisible: !message }"
    type="error"
    variant="text"
    class="ma-0 pa-0 fixed-height"
    density="compact"
    :icon="false"
  >
    <template #prepend>
      <v-icon size="22" color="error">mdi-alert-circle</v-icon>
    </template>
    {{ message }}
  </v-alert>
</template>

<script setup>
defineProps({
  message: {
    type: String,
    default: ''
  }
})
</script>

<style scoped>
.fixed-height {
  min-height: 23px;
  font-size: 12px;
  font-weight: bold;
}

.invisible {
  visibility: hidden;
}
</style>