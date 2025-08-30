import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_ADDRESS, CONF_UPDATE_INTERVAL
from esphome.core import coroutine_with_priority

from esphome.components import modbus

CODEOWNERS = ["@esphome/core"]

DEPENDENCIES = ["modbus"]

CONF_MODBUS_ID = "modbus_id"

modbus_controller2_ns = cg.esphome_ns.namespace("modbus_controller2")
ModbusController2 = modbus_controller2_ns.class_("ModbusController2", cg.Component)

CONFIG_SCHEMA = cv.ensure_list(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(ModbusController2),
            cv.Required(CONF_ADDRESS): cv.int_,
            cv.Required(CONF_MODBUS_ID): cv.use_id(modbus.ModbusDevice),
            cv.Optional(CONF_UPDATE_INTERVAL, default="1s"): cv.update_interval,
        }
    ).extend(cv.COMPONENT_SCHEMA)
)

@coroutine_with_priority(40.0)
async def to_code(config):
    for conf in config:
        var = cg.new_Pvariable(conf[CONF_ID])
        await cg.register_component(var, conf)
        parent = await cg.get_variable(conf[CONF_MODBUS_ID])
        cg.add(var.set_modbus_parent(parent))
        cg.add(var.set_address(conf[CONF_ADDRESS]))
        cg.add(var.set_update_interval(conf[CONF_UPDATE_INTERVAL]))