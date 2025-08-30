import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import modbus
from esphome.const import CONF_ID, CONF_MODBUS_ID, CONF_ADDRESS, CONF_UPDATE_INTERVAL

DEPENDENCIES = ["modbus"]

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import modbus
from esphome.components.modbus import CONF_MODBUS_ID
from esphome.const import CONF_ID, CONF_ADDRESS, CONF_UPDATE_INTERVAL

DEPENDENCIES = ["modbus"]

modbus_controller2_ns = cg.esphome_ns.namespace("modbus_controller2")
ModbusController2 = modbus_controller2_ns.class_("ModbusController2", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ModbusController2),
    cv.Required(CONF_MODBUS_ID): cv.use_id(modbus.ModbusDevice),
    cv.Required(CONF_ADDRESS): cv.int_,
    cv.Optional(CONF_UPDATE_INTERVAL, default="1s"): cv.update_interval,
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    modbus_dev = await cg.get_variable(config[CONF_MODBUS_ID])
    cg.add(var.set_modbus_id(modbus_dev))

    cg.add(var.set_address(config[CONF_ADDRESS]))
    cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL]))