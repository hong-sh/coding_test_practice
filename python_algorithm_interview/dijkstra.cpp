#include<queue>
#include<vector>
#include<map>
#include<string>

using namespace std;


map<string, vector<pair<string, int>>*> graph;
map<string, int> dist;

void dijkstra()
{
	priority_queue<pair<string, int>> PQ;
	PQ.push(make_pair("A", 0));

	while (PQ.empty() == 0)
	{
		string current = PQ.top().first;
		int cost = -PQ.top().second;
		PQ.pop();

		vector<pair<string, int>>::iterator iter;
		for (iter = graph[current]->begin(); iter != graph[current]->end(); iter++)
		{
			string next = (*iter).first;
			int next_cost = (*iter).second;

			if (dist[next] > cost + next_cost)
			{
				dist[next] = cost + next_cost;
				PQ.push(make_pair(next, -dist[next]));
			}
		}
	}
}

int main()
{

	graph.insert_or_assign("A", new vector<pair<string, int>>());
	graph.insert_or_assign("B", new vector<pair<string, int>>());
	graph.insert_or_assign("C", new vector<pair<string, int>>());
	graph.insert_or_assign("D", new vector<pair<string, int>>());
	graph.insert_or_assign("E", new vector<pair<string, int>>());

	graph["A"]->push_back(make_pair("B", 4));
	graph["A"]->push_back(make_pair("C", 1));

	graph["B"]->push_back(make_pair("E", 4));
	
	graph["C"]->push_back(make_pair("B", 2));
	graph["C"]->push_back(make_pair("D", 4));

	graph["D"]->push_back(make_pair("E", 4));

	dist["A"] = 9999;
	dist["B"] = 9999;
	dist["C"] = 9999;
	dist["D"] = 9999;
	dist["E"] = 9999;

	dijkstra();
}
