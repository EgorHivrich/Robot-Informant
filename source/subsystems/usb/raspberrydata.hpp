#if not defined(__RAPSBERRY_DATA_HPP)
#define __RASPBERRY_DATA_HPP

#include <cstdint>
#include <fstream>

#define RASPBERRY_HEADER

struct RaspberryData {
    uint8_t data;
    uint8_t unused;
} __attribute__((packed));

#if defined(ARDUINO_HEADER)

class DataReciever {
public:
    DataReciever(void);
    ~DataReciever(void);

private:
    std::fstream _port;
};

#elif defined(RASPBERRY_HEADER)

class DataUploader {
public:
    DataUploader(void);
    ~DataUploader(void);

public:
    bool upload(const RaspberryData& data);

private:
    std::fstream _port;
};

#endif // arduino_header

#endif // raspberrydata.hpp