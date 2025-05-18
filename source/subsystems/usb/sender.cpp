#include "raspberrydata.hpp"

DataUploader::DataUploader(void)
  : _port("COM1", std::ios_base::in) { }

bool DataUploader::upload(const RaspberryData& data)
{
    try {
        _port.write(reinterpret_cast<const char*>(&data), sizeof(RaspberryData));
        return true;
    } catch(const std::exception& exception) {
        return false;
    }
    return false;
}

DataUploader::~DataUploader(void) { _port.close(); }