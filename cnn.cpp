
#include <iostream>
#include "cnn.h"
using namespace std;

typedef std::vector<Neuron> Layer;

Net::Net(const std::vector <unsigned> &topology ) {

   unsigned numLayers = topology.size();

   for ( unsigned layerNum = 0; layerNum < numLayers; ++layerNum ) {
      m_layers.push_back( Layer() );
      unsigned numOutputs = layerNum == topology.size() - 1 ? 0 : topology[layerNum + 1];
      for ( unsigned NeuronNum = 0; NeuronNum <= topology[layerNum]; ++NeuronNum )
      {
         m_layers.back().push_back( Neuron(numOutputs) );
         cout << "Made a neuron" << endl;
      }
   }
}

void Net::feedForward(const std::vector<double> &inputVals ) {}

void Net::backProp( const std::vector<double> &targetVals ) {}

void Net::getResults( std::vector<double> &resultVals ) {}
