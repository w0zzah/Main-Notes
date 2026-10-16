#include "bulb.h"
#include <stdint.h>
#include <stdio.h>

static uint8_t sold[225] = {0};

Bulb bulb_sellModel(uint8_t model)
{
    Bulb bulb = {
        .model = model,
        .serialNumber = sold[model]
    };
    sold[model] += 1;
    return bulb;
}

void bulb_display(Bulb bulb)
{
    printf("Model %u, SN%.6u\n", bulb.model, bulb.serialNumber);
}

uint32_t bulb_numSold(uint8_t model)
{
    return sold[model];
}