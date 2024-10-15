import React, { useState } from 'react';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomePage from './app/HomePage';
import CategoryItems from './app/CategoryItems';


const Stack = createStackNavigator();

const App = () => {
  // State to store the list of categories
  const [categories, setCategories] = useState([]);

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen 
          name="HomePage"
          options={{ title: 'Inventory Tracker' }}
        >
          {props => (
            <HomePage {...props} categories={categories} setCategories={setCategories} />
          )}
        </Stack.Screen>
        <Stack.Screen 
          name="CategoryItems"
          component={CategoryItems}
          options={({ route }) => ({ title: route.params.categoryName })}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
