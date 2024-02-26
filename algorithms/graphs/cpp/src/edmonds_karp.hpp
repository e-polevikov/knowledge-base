#include <vector>

struct EdgeFlow {
    int vtxFrom;
    int vtxTo;
    int value;

    EdgeFlow(int vtxFrom, int vtxTo, int value)
        : vtxFrom(vtxFrom)
        , vtxTo(vtxTo)
        , value(value)
    { }
};

struct Flow {
    int value;
    std::vector<EdgeFlow> edges;

    explicit Flow(int value) : value(value) { }
};

Flow edmondsKarp(
    const std::vector<std::vector<std::pair<int, int>>> &network
);
