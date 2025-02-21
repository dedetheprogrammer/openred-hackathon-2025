<script setup>
  import { ref } from 'vue';
  import { NButton, NIcon, NSpace, NCard, NTag, NText, NDescriptions, NDescriptionsItem } from "naive-ui";

  const UUIDService = "e63215e5-7003-49d8-96b0-b024798fb901"
  const UUIDServiceChar1 = "e63215e6-7003-49d8-96b0-b024798fb901"
  const UUIDServiceChar2 = "e63215e7-7003-49d8-96b0-b024798fb901"
  
  let intervalId = undefined;

  let data = ref(null)
  const bleDevice = ref(null);
  const isConnected = ref(false);

  // Connect device
  const connectDevice = () => {
    try {
      requestBlE();
    } catch (error) {
      console.error("Request BLE : " + error);
    }
  };

  const disconnectDevice = () => {
    isConnected.value = false;
    if (!bleDevice.value) {
      return;
    }
    if (bleDevice.value.gatt.connected) {
      bleDevice.value.gatt.disconnect();
    } else {
      console.warn("Bluetooth Device is already disconnected");
    }
  };


  const onDisconnected = () => {
    console.log("Device is disconnected.");
    isConnected.value = false;
    clearInterval(intervalId)
  };

  // Request connection to a Pinetime device
  const requestBlE = () => {
    if (navigator.bluetooth == undefined) {
      console.error("Sorry, Your device does not support Web BLE!");
      return;
    }

    navigator.bluetooth
      .requestDevice({
        filters: [
          {
            namePrefix: "RadiaCode",
          },
        ],
        optionalServices: [UUIDService],
      })
      .then((device) => {
        bleDevice.value = device;
        bleDevice.value.addEventListener("gattserverdisconnected", onDisconnected);
        return bleDevice.value.gatt.connect();
      })
      .then(async (server) => {
        if (server) {
          getDeviceCharacteristic();
          isConnected.value = true;
        }
      })
      .catch((error) => {
        console.error("BLE Connection : " + error);
        isConnected.value = false;
      });
  };

  const getDeviceCharacteristic = () => {
    const a = bleDevice.value.gatt
      .getPrimaryService(UUIDService)
      .then(async (service) => {
        try {
          const characteristic1 = await service.getCharacteristic(UUIDServiceChar1);
          await characteristic1.writeValue(new Uint8Array([0x04, 0x00, 0x00, 0x00, 0x0b, 0x00, 0x00, 0x80]))
          intervalId = setInterval(async () => {
            await characteristic1.writeValue(new Uint8Array([0x04, 0x00, 0x00, 0x00, 0x0b, 0x00, 0x00, 0x80]))
          }, 1000)
          // Add the event listener before starting notifications
          const characteristic2 = await service.getCharacteristic(UUIDServiceChar2);
          characteristic2.addEventListener('characteristicvaluechanged', handleNotification);
          // Start notifications
          await characteristic2.startNotifications();
          console.log("Notificaciones habilitadas para la característica");
        } catch (error) {
          console.error("Error al habilitar notificaciones o agregar el listener:", error);
        }
      })
      .catch((error) => {
        console.error("getDeviceCharacteristic: " + error);
        disconnectDevice();
      });
  }


  const handleNotification = async (event) => {
    // Si el valor es una cadena de texto (si el valor es un UTF-8)
    const text = new TextDecoder().decode(event.target.value);
    data = text;
    console.log("Text:", text);
  }
</script>

<style scoped>
  main {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
  }

  .buttons {
    width: 150px;
  }
</style>

<template>
  <main>
    <n-tag v-if="data" type="primary">{{ data }}</n-tag>
    <n-button class="buttons" type="success" @click="connectDevice">
      Connect to&nbsp;<b>device</b>
    </n-button>
    <n-button v-if="isConnected" class="buttons" type="error" @click="disconnectDevice">
      Disconnect
    </n-button>
  </main>
</template>
