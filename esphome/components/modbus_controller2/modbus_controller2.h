#include "modbus_controller2.h"
#include "esphome/core/log.h"

namespace esphome {
namespace modbus_controller2 {

static const char *const TAG = "modbus_controller2";

void ModbusController2::setup() {
  ESP_LOGI(TAG, "ModbusController2 setup at address %d", address_);
}

void ModbusController2::loop() {
  // contoh log
  ESP_LOGV(TAG, "Polling modbus device %d ...", address_);
  // nanti di sini bisa ditambahkan request Modbus
}

}  // namespace modbus_controller2
}  // namespace esphome