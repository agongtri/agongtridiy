#pragma once
#include "esphome/core/component.h"
#include "esphome/core/hal.h"

namespace esphome {
namespace modbus_controller2 {

class ModbusController2 : public Component {
 public:
  void setup() override;
  void loop() override;
};

}  // namespace modbus_controller2
}  // namespace esphome
