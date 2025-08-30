#pragma once
#include "esphome/core/component.h"
#include "esphome/components/modbus/modbus.h"

namespace esphome {
namespace modbus_controller2 {

class ModbusController2 : public Component {
 public:
  void set_address(uint8_t address) { address_ = address; }
  void set_modbus_id(modbus::Modbus *modbus_parent) { modbus_parent_ = modbus_parent; }
  void set_update_interval(uint32_t update_interval) { update_interval_ = update_interval; }

  void setup() override {
    ESP_LOGI("modbus_controller2", "Setup with address %d", address_);
  }

  void loop() override {
    // TODO: implement polling / request
  }

 protected:
  uint8_t address_;
  modbus::Modbus *modbus_parent_;
  uint32_t update_interval_;
};

}  // namespace modbus_controller2
}  // namespace esphome