- No extra explanations or comments

// FILE: main.go
package main

import (
	"fmt"
	"runtime"
	"sync"
)

// StorageOperate represents the storage operator connection.
type StorageOperate struct {
	id int64
}

// Close releases the storage operator connection back to the pool.
func (s *StorageOperate) Close() error {
	// Simulate releasing connection/resources
	return nil
}

// RegistryClient simulates the ZooKeeper/Curator registry client.
type RegistryClient struct {
	mu        sync.Mutex
	listeners map[string]func()
}

func NewRegistryClient() *RegistryClient {
	return &RegistryClient{
		listeners: make(map[string]func()),
	}
}

func (r *RegistryClient) AddListener(key string, listener func()) {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.listeners[key] = listener
}

func (r *RegistryClient) RemoveListener(key string) {
	r.mu.Lock()
	defer r.mu.Unlock()
	delete(r.listeners, key)
}

// ThreadLocalContext simulates thread-local storage.
type dataMap struct {
	sync.Mutex
	data map[string]interface{}
}

var contextMap = dataMap{
	data: make(map[string]interface{}),
}

func SetContext(key string, val interface{}) {
	contextMap.Lock()
	defer contextMap.Unlock()
	contextMap.data[key] = val
}

func ClearContext() {
	contextMap.Lock()
	defer contextMap.Unlock()
	contextMap.data = make