import React, { useState } from 'react';
import { View, Text, TextInput, FlatList, TouchableOpacity, Modal, Button } from 'react-native';
import { styles } from '../styles/styles'; // Assuming you have a separate styles.js file

const HomePage = ({ navigation, categories, setCategories }) => {
  const [modalVisible, setModalVisible] = useState(false);  // To control the modal visibility
  const [newCategory, setNewCategory] = useState('');

  // Function to handle adding a new category
  const addCategory = () => {
    if (newCategory.trim() !== '') {
      setCategories([...categories, { id: Date.now().toString(), name: newCategory }]);
      setNewCategory('');
      setModalVisible(false);  // Close the modal after adding the category
    }
  };

  return (
    <View style={styles.container}>
      {/* If no categories, show the + button in the center */}
      {categories.length === 0 ? (
        <TouchableOpacity onPress={() => setModalVisible(true)} style={styles.centeredAddButton}>
          <Text style={styles.buttonText}>+</Text>
        </TouchableOpacity>
      ) : (
        // FlatList to render categories and a + button at the end if categories exist
        <FlatList
          data={[...categories, { id: 'add', name: '+' }]}  // Add the + button at the end of the list
          keyExtractor={item => item.id}
          renderItem={({ item }) =>
            item.id === 'add' ? (
              <TouchableOpacity onPress={() => setModalVisible(true)} style={styles.addButton}>
                <Text style={styles.buttonText}>+</Text>
              </TouchableOpacity>
            ) : (
              <TouchableOpacity
                onPress={() => navigation.navigate('CategoryItems', { categoryId: item.id, categoryName: item.name })}
                style={styles.categoryButton}  // Apply square red button style
              >
                <Text style={styles.buttonText}>{item.name}</Text>
              </TouchableOpacity>
            )
          }
          numColumns={3}  // Display buttons in a grid with 3 columns
          columnWrapperStyle={styles.columnWrapper}
        />
      )}

      {/* Modal for adding a new category */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalView}>
          <TextInput
            placeholder="Enter new category"
            value={newCategory}
            onChangeText={setNewCategory}
            style={styles.input}
          />
          <Button title="Add Category" onPress={addCategory} />
          <Button title="Cancel" onPress={() => setModalVisible(false)} />
        </View>
      </Modal>
    </View>
  );
};

export default HomePage;