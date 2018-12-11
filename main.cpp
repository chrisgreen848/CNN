#include <iostream>
#include <vector>
#include "cnn.H"
using namespace std;

int main() {
   vector<unsigned> topology;
   topology.push_back( 3 );
   topology.push_back( 2 );
   topology.push_back( 1 );
   Net newNetwork( topology );

   vector<double> inputVals;
   newNetwork.feedForward(inputVals);
   vector<double> targetVals;
   newNetwork.backProp( targetVals);
   vector<double> resultVals;
   newNetwork.getResults(resultVals);

   int end;
   cin >> end;

}
